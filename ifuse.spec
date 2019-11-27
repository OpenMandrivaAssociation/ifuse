Name:		ifuse
Version:	1.1.3
Release:	8
Summary:	Mount Apple iPhone and iPod touch devices
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
Patch0:        ifuse-1.1.3-upstream-fixes-20181008.patch
BuildRequires: pkgconfig(fuse)
BuildRequires: pkgconfig(libimobiledevice-1.0)
BuildRequires: pkgconfig(libplist)

%description
A fuse filesystem for mounting iPhone and iPod touch devices

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING README
%{_bindir}/ifuse
%{_mandir}/man1/*
