# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lru
%global full_version 0.16.4
%global pkgname lru-0.16

Name:           rust-lru-0.16
Version:        0.16.4
Release:        %autorelease
Summary:        Rust crate "lru"
License:        MIT
URL:            https://github.com/jeromefroe/lru-rs
#!RemoteAsset:  sha256:7f66e8d5d03f609abc3a39e6f08e4164ebf1447a732906d39eb9b99b7919ef39
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(lru) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "lru"

%package     -n %{name}+hashbrown
Summary:        LRU cache implementation - feature "hashbrown" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(hashbrown-0.16/default) >= 0.16.1
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/hashbrown)

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust lru crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+nightly
Summary:        LRU cache implementation - feature "nightly"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/hashbrown)
Requires:       crate(hashbrown-0.16/nightly) >= 0.16.1
Provides:       crate(%{pkgname}/nightly)

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust lru crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
