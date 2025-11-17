# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           itstool
Version:        2.0.7
Release:        %autorelease
Summary:        ITS-based XML translation tool
License:        GPL-3.0-or-later
URL:            http://itstool.org/
#!RemoteAsset
Source0:        http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2
Patch0001:      0001-Fix-insufficiently-quoted-regular-expressions.patch
Patch0002:      0002-Switch-from-libxml2-to-lxml.patch

BuildSystem:    autotools

BuildArch:      noarch

BuildRequires:  python3-lxml
BuildRequires:  python3-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Requires:       python3-lxml
BuildOption(prep): -n %{name}-%{version} -p1
%description
ITS Tool allows you to translate XML documents with PO files, using rules from
the W3C Internationalization Tag Set (ITS) to determine what to translate and
how to separate it into PO file messages

%conf -p
autoreconf -fi
export PYTHON=%{__python3}

%files
%license COPYING COPYING.GPL3
%doc ChangeLog NEWS
%{_bindir}/itstool
%{_datadir}/itstool
%{_mandir}/man1/*

%changelog
%{?autochangelog}
