%define		_class		Text
%define		_subclass	Wiki
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.2.1
Release:	4
Summary:	Parsing and rendering rules for Wiki markup in structured text
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Text_Wiki/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Abstracts parsing and rendering rules for Wiki markup in structured
plain text.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-3mdv2012.0
+ Revision: 742293
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2
+ Revision: 679597
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-1mdv2011.0
+ Revision: 594503
- update to new version 1.2.1

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-5mdv2010.1
+ Revision: 466328
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.0-4mdv2010.0
+ Revision: 441662
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3mdv2009.1
+ Revision: 322698
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdv2009.0
+ Revision: 237154
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 23 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1mdv2008.0
+ Revision: 54564
- 1.2.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdv2007.0
+ Revision: 82761
- Import php-pear-Text_Wiki

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdk
- 1.1.0

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-1mdk
- 1.0.3
- new group (Development/PHP)

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdk
- 1.0.1

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdk
- initial Mandriva package (PLD import)

