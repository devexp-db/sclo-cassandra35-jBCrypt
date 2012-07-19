Name:           jBCrypt
Version:        0.3
Release:        7%{?dist}
Summary:        Strong password hashing for Java

Group:          Development/Libraries
License:        ISC
URL:            http://www.mindrot.org/projects/jBCrypt/
Source0:        http://www.mindrot.org/files/jBCrypt/jBCrypt-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  junit

Requires:       java
Requires:       jpackage-utils  

%description
A Java implementation of OpenBSD's Blowfish password hashing code. 


%prep
%setup -q


%build
javac BCrypt.java
jar cvf jBCrypt.jar BCrypt.class

# compile test cases too
javac -encoding UTF-8 -cp %{_javadir}/junit.jar:jBCrypt.jar TestBCrypt.java
jar cvf jBCrypt-test.jar TestBCrypt.class


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp jBCrypt.jar $RPM_BUILD_ROOT%{_javadir}/jBCrypt.jar


%check
java -cp %{_javadir}/junit.jar:jBCrypt.jar:jBCrypt-test.jar TestBCrypt


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE README
%{_javadir}/%{name}.jar


%changelog
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
