# Tarfile created using git
# git clone http://git.matt.colyer.name/2008/ifuse/
# git-archive --format=tar --prefix=ifuse-0.1.0/ %{git_version} | bzip2 > ifuse-0.1.0-%{gitdate}.tar.bz2

%define gitdate 20081214
%define git_version b0412bf
%define tarfile %{name}-%{version}-%{gitdate}.tar.bz2
%define snapshot %{gitdate}git%{git_version}

Name:          ifuse
Version:       0.1.0
Release:       %{snapshot}.%mkrel 1
Summary:       Mount Apple iPhone and iPod touch devices

Group:         System/Libraries
License:       GPLv2+
URL:           http://matt.colyer.name/projects/iphone-linux/
Source0:       %{tarfile}
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires:      hal
BuildRequires: glib2-devel
BuildRequires: fuse-devel
BuildRequires: libiphone-devel

# Require these until a formal release
BuildRequires: libtool
BuildRequires: automake
BuildRequires: autoconf

%description
A fuse filesystem for mounting iPhone and iPod touch devices

%prep
%setup -q

%build
./autogen.sh
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
/sbin/mount.fuse.ifuse
%{_bindir}/hal-iphone-setup
%{_datadir}/hal/fdi/information/20thirdparty/30-ifuse.fdi
