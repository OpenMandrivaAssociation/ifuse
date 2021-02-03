Name:		ifuse
Version:	02022021
Release:	1
Summary:	Mount Apple iPhone and iPod touch devices
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(fuse)
BuildRequires: pkgconfig(libimobiledevice-1.0)
BuildRequires: pkgconfig(libplist-2.0)

%description
A fuse filesystem for mounting iPhone and iPod touch devices

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING README.md
%{_bindir}/ifuse
%{_mandir}/man1/*
