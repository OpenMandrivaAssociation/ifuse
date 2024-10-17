%define	git	20230802 

Name:		ifuse
Version:	1.1.5
Release:	%{?git:0.%{git}.}1
Summary:	Mount Apple iPhone and iPod touch devices
Group:		System/Libraries
License:	GPLv2+
URL:		https://www.libimobiledevice.org/
%if 0%{?git:1}
Source0:	https://github.com/libimobiledevice/ifuse/archive/refs/heads/master.tar.gz#/%{name}-%{git}.tar.gz
%else
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.xz
%endif

BuildRequires: pkgconfig(fuse)
BuildRequires: pkgconfig(libimobiledevice-1.0)
BuildRequires: pkgconfig(libplist-2.0)

%description
A fuse filesystem for mounting iPhone and iPod touch devices

%prep
%autosetup -p1 -n %{name}-%{?git:master}%{!?git:%{version}}
./autogen.sh
%configure

%build
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING README.md
%{_bindir}/ifuse
%{_mandir}/man1/*
