# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           labwc
Version:        0.9.3
Release:        %autorelease
Summary:        A Wayland window-stacking compositor
License:        GPL-2.0-only
URL:            https://github.com/labwc/labwc
#!RemoteAsset:  sha256:38d273faa4e021b9f99e1bf1a5f4bf881cc6a592e00c7b3426b37c0a0b67d126
Source0:        https://github.com/labwc/labwc/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dxwayland=disabled

BuildRequires:  meson >= 0.59.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libinput) >= 1.14
BuildRequires:  pkgconfig(libsfdo-basedir)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server) >= 0.19.0
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)

Requires:       xdg-desktop-portal-wlr

%description
Labwc is a wlroots-based window-stacking compositor for wayland, inspired by
openbox. It is light-weight and independent with a focus on simply stacking
windows well and rendering some window decorations.

%install -a
# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/en_GB/
%find_lang %{name} --generate-subpackages

%files
%license LICENSE
%doc NEWS.md
%{_bindir}/labwc
%{_bindir}/lab-sensible-terminal
%{_bindir}/labnag
%{_docdir}/labwc
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_datadir}/xdg-desktop-portal/labwc-portals.conf
%{_datadir}/wayland-sessions/labwc.desktop
%{_datadir}/icons/hicolor/*/*/labwc*.svg

%changelog
%{?autochangelog}
