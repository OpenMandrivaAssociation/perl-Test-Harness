%define modname	Test-Harness
%define modver	3.26

Summary:	Run Perl standard test scripts with statistics
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std
# rename prove to avoid conflict with perl
mv %{buildroot}/%{_bindir}/prove %{buildroot}/%{_bindir}/prove-%{modver}
# rename mandir files to avoid conflict with regular Mandriva perl
find %{buildroot}%{_mandir} -type f -exec mv {} {}-%{modver} \;

%check
%make test

%files
%doc Changes
%{_bindir}/prove-%{modver}
%{perl_vendorlib}/Test
%{perl_vendorlib}/TAP
%{perl_vendorlib}/App
%{_mandir}/man1/*
%{_mandir}/man3/*

