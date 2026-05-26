# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parking
%global full_version 2.2.1
%global pkgname parking-2.0

Name:           rust-parking-2.0
Version:        2.2.1
Release:        %autorelease
Summary:        Rust crate "parking"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/parking
#!RemoteAsset:  sha256:f38d5652c16fde515bb1ecef450ab0f6a219d619a7274976324d5e377f7dceba
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(parking) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "parking"

%package     -n %{name}+loom
Summary:        Thread parking and unparking - feature "loom"
Requires:       crate(%{pkgname})
Requires:       crate(loom-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/loom)

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust parking crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
