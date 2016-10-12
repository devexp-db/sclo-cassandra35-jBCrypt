%{?scl:%scl_package jBCrypt}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}jBCrypt
Version:	0.4
Release:	2%{?dist}
Summary:	Strong password hashing for Java
License:	ISC
URL:		http://www.mindrot.org/projects/%{pkg_name}
Source0:	http://www.mindrot.org/files/%{pkg_name}/%{pkg_name}-%{version}.tar.gz

BuildRequires:	%{?scl_prefix_java_common}ant
BuildRequires:	%{?scl_prefix_java_common}ant-junit
BuildRequires:	%{?scl_prefix_java_common}javapackages-local
BuildRequires:	%{?scl_prefix_java_common}junit
%{?scl:Requires: %scl_runtime}

BuildArch:	noarch

%description
A Java implementation of OpenBSD's Blowfish password hashing code. 

%package javadoc
Summary:	API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{pkg_name}-%{version}

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_file : %{pkg_name}/%{pkg_name} %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
ant test dist
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_artifact 'org.mindrot:jbcrypt:0.4' jbcrypt.jar
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE

%changelog
* Wed Oct 12 2016 Tomas Repik <trepik@redhat.com> - 0.4-2
- use standard SCL macros

* Tue Jul 26 2016 Pavel Raiskup <praiskup@redhat.com> - 0.4-1
- basic scl movement
