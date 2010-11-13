%define upstream_name    Test-Harness
%define upstream_version 3.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Run Perl standard test scripts with statistics
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# rename prove to avoid conflict with perl
mv %{buildroot}/%{_bindir}/prove %{buildroot}/%{_bindir}/prove-%{upstream_version}
# rename mandir files to avoid conflict with regular Mandriva perl
find %{buildroot}/%{_mandir} -type f -exec mv {} {}-%{upstream_version} \;

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
%{_bindir}/prove-%{upstream_version}
