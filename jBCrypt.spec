Name:           jBCrypt
Version:        0.4
Release:        1%{?dist}
Summary:        Strong password hashing for Java

License:        ISC
URL:            http://www.mindrot.org/projects/jBCrypt
Source0:        http://www.mindrot.org/files/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  javapackages-local
BuildRequires:  junit

Obsoletes:      %{name}-javadoc < %{version}-%{release}

%description
A Java implementation of OpenBSD's Blowfish password hashing code. 

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%mvn_file : %{name}/%{name} %{name}

%build
ant test dist

%install
%mvn_artifact 'org.mindrot:jbcrypt:0.4' jbcrypt.jar
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE

%changelog
* Mon Mar 02 2015 Michal Srb <msrb@redhat.com> - 0.4-1
- Update to upstream version 0.4
- Resolves: CVE-2015-0886

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.3-11
- Use Requires: java-headless rebuild (#1067528)

* Fri Oct 18 2013 Michal Srb <msrb@redhat.com> - 0.3-10
- Adapt to current packaging guidelines
- Add javadoc subpackage
- Build with Maven

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 17 2012 Deepak Bhole <dbhole@redhat.com> 0.3-6
- Resolves rhbz#788720
- Patch from Omair Majid <omajid@redhat.com>:
  - Fix for building with OpenJDK7 by explicitly specifying the encoding

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 22 2010 Sebastian Dziallas <sebastian@when.com> - 0.3-3
- follow upstream naming for the package
- add %check section and compile tests

* Thu Jun 17 2010 Sebastian Dziallas <sebastian@when.com> - 0.3-2
- let's package the class file instead of the jar one

* Sat May 08 2010 Sebastian Dziallas <sebastian@when.com> - 0.3-1
- initial update to try new stable branch
