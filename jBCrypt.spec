%{?scl:%scl_package jBCrypt}
%{!?scl:%global pkg_name %{name}}

Name:          %{?scl_prefix}jBCrypt
Version:       0.4
Release:       1%{?dist}
Summary:       Strong password hashing for Java

License:       ISC
URL:           http://www.mindrot.org/projects/%{pkg_name}
Source0:       http://www.mindrot.org/files/%{pkg_name}/%{pkg_name}-%{version}.tar.gz

BuildRequires: %{?scl_java_prefix}ant
BuildRequires: %{?scl_java_prefix}ant-junit
BuildRequires: %{?scl_java_prefix}javapackages-local
BuildRequires: %{?scl_java_prefix}junit
%{?scl:Requires: %scl_runtime}

BuildArch:     noarch

%description
A Java implementation of OpenBSD's Blowfish password hashing code. 

%package       javadoc
Summary:       API documentation for %{name}

%description   javadoc
This package contains the API documentation for %{name}.

%prep
%{?scl_enable}
%setup -q -n %{pkg_name}-%{version}

%mvn_file : %{pkg_name}/%{pkg_name} %{pkg_name}
%{?scl_disable}

%build
%{?scl_enable}
ant test dist
%{?scl_disable}

%install
%{?scl_enable}
%mvn_artifact 'org.mindrot:jbcrypt:0.4' jbcrypt.jar
%mvn_install
%{?scl_disable}

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Jul 26 2016 Pavel Raiskup <praiskup@redhat.com> - 0.4-1
- basic scl movement
