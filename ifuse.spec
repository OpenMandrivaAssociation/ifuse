Name:		ifuse
Version:	1.1.3
Release:	6
Summary:	Mount Apple iPhone and iPod touch devices
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
Patch0:		ifuse-1.1.1-fix-link.patch
BuildRequires:	fuse-devel
BuildRequires:	libimobiledevice-devel >= 1.1.6

%description
A fuse filesystem for mounting iPhone and iPod touch devices

%prep
%setup -q
#%patch0 -p0

%build
%configure
%make

%install
%makeinstall_std DESTDIR=%{buildroot}

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/ifuse.1.*
