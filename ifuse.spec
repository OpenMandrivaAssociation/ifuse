Name:          ifuse
Version:       1.1.3
Release:       %mkrel 3
Summary:       Mount Apple iPhone and iPod touch devices

Group:         System/Libraries
License:       GPLv2+
URL:           http://www.libimobiledevice.org/
Source0:       http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
Patch0:        ifuse-1.1.1-fix-link.patch
BuildRequires: fuse-devel
BuildRequires: libimobiledevice-devel >= 1.0.0

%description
A fuse filesystem for mounting iPhone and iPod touch devices

%prep
%setup -q
#%patch0 -p0

%build
%configure2_5x
%make

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/ifuse.1.*


%changelog
* Sat May 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.2-1mdv2012.0
+ Revision: 799608
- version update 1.1.2

* Tue Apr 05 2011 Funda Wang <fwang@mandriva.org> 1.1.1-1
+ Revision: 650604
- new version 1.1.1

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2011.0
+ Revision: 611175
- rebuild

* Mon Mar 22 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.0.0-1mdv2010.1
+ Revision: 526327
- ifuse 1.0.0

* Tue Feb 02 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.9.7-1mdv2010.1
+ Revision: 499519
- new release

* Mon Dec 07 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.5-2mdv2010.1
+ Revision: 474469
- rebuild against new libplist

* Tue Nov 24 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.5-1mdv2010.1
+ Revision: 469736
- 0.9.5 release

* Fri Nov 06 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.4-1mdv2010.1
+ Revision: 460547
- New version: 0.9.4

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0.1.0-20081214gitb0412bf.1mdv2009.1
+ Revision: 333139
- import ifuse

