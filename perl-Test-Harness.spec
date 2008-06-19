%define module  Test-Harness
%define name    perl-%{module}
%define version 3.11
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Run Perl standard test scripts with statistics
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
STOP! If all you want to do is write a test script, consider using
Test::Simple. Test::Harness is the module that reads the output from
Test::Simple, Test::More and other modules based on Test::Builder. You don't
need to know about Test::Harness to use those modules.

Test::Harness runs tests and expects output from the test in a certain format.
That format is called TAP, the Test Anything Protocol. It is defined in
Test::Harness::TAP.

Test::Harness::runtests(@tests) runs all the testscripts named as arguments and
checks standard output for the expected strings in TAP format.

The prove utility is a thin wrapper around Test::Harness.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# rename prove to avoid conflict with perl
mv %{buildroot}/%{_bindir}/prove %{buildroot}/%{_bindir}/prove-%{version}
# rename mandir files to avoid conflict with regular Mandriva perl
find %{buildroot}/%{_mandir} -type f -exec mv {} {}-%{version} \;

%check
%make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Test
%{perl_vendorlib}/TAP
%{perl_vendorlib}/App
%{_mandir}/*/*
%{_bindir}/prove-%{version}
