%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	NetworkManager VPN integration for OpenSWAN
Name:		networkmanager-openswan
Version:	1.0.8
Release:	ZED'S DEAD
License:	GPLv2+
Group:		System/Base
Url:		https://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openswan/%{url_ver}/NetworkManager-openswan-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	perl-XML-Parser
BuildRequires:	perl
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnm-gtk)
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-glib-vpn)
BuildRequires:	pkgconfig(libnl-3.0)
BuildRequires:	pkgconfig(libsecret-unstable)
Requires:	dbus
Requires:	GConf2
Requires:	gnome-keyring
Requires:	gtk+3
Requires:	NetworkManager
Requires:	shared-mime-info

%description
This package contains software for integrating the OpenSWAN IPSec VPN software
with NetworkManager and the GNOME desktop.

%prep
%setup -qn NetworkManager-openswan-%{version}
%autopatch -p1

%build
%configure \
	--disable-static \
	--disable-dependency-tracking

%make

%install
%makeinstall_std

%find_lang NetworkManager-openswan

%files -f NetworkManager-openswan.lang
%doc AUTHORS ChangeLog README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-openswan-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-openswan-service.name
%{_libdir}/NetworkManager/libnm-openswan-properties.so
%{_libexecdir}/nm-openswan-auth-dialog
%{_libexecdir}/nm-openswan-service
%{_libexecdir}/nm-openswan-service-helper
%{_datadir}//gnome-vpn-properties/openswan/nm-openswan-dialog.ui

