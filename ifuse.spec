Name:          ifuse
Version:       1.1.1
Release:       %mkrel 1
Summary:       Mount Apple iPhone and iPod touch devices

Group:         System/Libraries
License:       GPLv2+
URL:           http://www.libimobiledevice.org/
Source0:       http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
Patch0:        ifuse-1.1.1-fix-link.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: fuse-devel
BuildRequires: libimobiledevice-devel >= 1.0.0

%description
A fuse filesystem for mounting iPhone and iPod touch devices

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/%{name}
