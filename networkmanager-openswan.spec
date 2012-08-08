Summary:	NetworkManager VPN integration for OpenSWAN
Name:		networkmanager-openswan
Version:	0.9.6.0
Release:	1
License:	GPLv2+
Group:		System/Base
URL:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openswan/NetworkManager-openswan-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	perl-XML-Parser
BuildRequires:	perl
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-glib-vpn)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
Requires:	gtk+3
Requires:	dbus
Requires:	NetworkManager
Requires:	shared-mime-info
Requires:	GConf2
Requires:	gnome-keyring

%description
This package contains software for integrating the OpenSWAN IPSec VPN software
with NetworkManager and the GNOME desktop.

%prep
%setup -qn NetworkManager-openswan-%{version}
%apply_patches

%build
%configure2_5x \
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
%{_libexecdir}/nm-openswan-auth-dialog
%{_libexecdir}/nm-openswan-service

