%define upstream_name    Test-Harness
%define upstream_version 3.26

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Run Perl standard test scripts with statistics
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std
# rename prove to avoid conflict with perl
mv %{buildroot}/%{_bindir}/prove %{buildroot}/%{_bindir}/prove-%{upstream_version}
# rename mandir files to avoid conflict with regular Mandriva perl
find %{buildroot}%{_mandir} -type f -exec mv {} {}-%{upstream_version} \;

%check
%make test

%files
%doc Changes
%{perl_vendorlib}/Test
%{perl_vendorlib}/TAP
%{perl_vendorlib}/App
%{_mandir}/*/*
%{_bindir}/prove-%{upstream_version}


%changelog
* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 3.220.0-2mdv2011.0
+ Revision: 597198
- rebuild

* Mon Aug 16 2010 Jérôme Quelin <jquelin@mandriva.org> 3.220.0-1mdv2011.0
+ Revision: 570310
- update to 3.22

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 3.210.0-3mdv2011.0
+ Revision: 562435
- rebuild

* Sat Jul 24 2010 Jérôme Quelin <jquelin@mandriva.org> 3.210.0-2mdv2011.0
+ Revision: 558165
- rebuild

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 3.210.0-1mdv2010.1
+ Revision: 498974
- update to 3.21

* Sun Jan 24 2010 Jérôme Quelin <jquelin@mandriva.org> 3.200.0-1mdv2010.1
+ Revision: 495426
- update to 3.20

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.17-1mdv2010.0
+ Revision: 373794
- update to new version 3.17

* Fri Feb 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.16-1mdv2009.1
+ Revision: 345495
- update to new version 3.16

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.14-1mdv2009.1
+ Revision: 292353
- update to new version 3.14

* Tue Aug 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.13-1mdv2009.0
+ Revision: 271054
- update to new version 3.13

* Mon Jun 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.12-1mdv2009.0
+ Revision: 230281
- update to new version 3.12

* Thu Jun 19 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.11-1mdv2009.0
+ Revision: 226198
- update to new version 3.11

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.10-1mdv2009.0
+ Revision: 193932
- update to new version 3.10

* Wed Feb 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.09-1mdv2008.1
+ Revision: 166952
- update to new version 3.09

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.07-1mdv2008.1
+ Revision: 156181
- update to new version 3.07

* Thu Jan 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.06-1mdv2008.1
+ Revision: 154003
- update to new version 3.06

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.05-1mdv2008.1
+ Revision: 138066
- update to new version 3.05

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.03-1mdv2008.1
+ Revision: 115893
- update to new version 3.03

* Mon Nov 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.02-1mdv2008.1
+ Revision: 110294
- new version


* Tue Mar 13 2007 Stéphane Téletchéa <steletch@mandriva.org> 2.64-2mdv2007.1
+ Revision: 142312
- Temporary hack for man pages, waiting after gold release for perl upgrade

* Tue Feb 27 2007 mandrake <mandrake> 2.64-1mdv2007.1
+ Revision: 126401

* Tue Feb 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.64-1mdv2007.1
- first mdv release

