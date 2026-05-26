# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nom
%global full_version 8.0.0
%global pkgname nom-8.0

Name:           rust-nom-8.0
Version:        8.0.0
Release:        %autorelease
Summary:        Rust crate "nom"
License:        MIT
URL:            https://github.com/rust-bakery/nom
#!RemoteAsset:  sha256:df9761775871bdef83bee530e60050f7e54b1105350d6884eb0fb4f46c2f9405
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2.0) >= 2.8.0
Provides:       crate(nom) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/docsrs)

%description
Source code for takopackized Rust crate "nom"

%package     -n %{name}+std
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(memchr-2.0/std) >= 2.8.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust nom crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
