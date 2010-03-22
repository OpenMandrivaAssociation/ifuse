Name:          ifuse
Version:       1.0.0
Release:       %mkrel 1
Summary:       Mount Apple iPhone and iPod touch devices

Group:         System/Libraries
License:       GPLv2+
URL:           http://matt.colyer.name/projects/iphone-linux/
Source0:       http://cloud.github.com/downloads/MattColyer/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires:      hal
BuildRequires: glib2-devel
BuildRequires: fuse-devel
BuildRequires: libimobiledevice-devel >= 1.0.0

# Require these until a formal release
BuildRequires: libtool
BuildRequires: automake
BuildRequires: autoconf

%description
A fuse filesystem for mounting iPhone and iPod touch devices

%prep
%setup -q

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
