# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name new_debug_unreachable
%global full_version 1.0.6
%global pkgname new-debug-unreachable-1.0

Name:           rust-new-debug-unreachable-1.0
Version:        1.0.6
Release:        %autorelease
Summary:        Rust crate "new_debug_unreachable"
License:        MIT
URL:            https://github.com/mbrubeck/rust-debug-unreachable
#!RemoteAsset:  sha256:650eef8c711430f1a879fdd01d4745a7deea475becfb90269c06775983bbf086
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(new-debug-unreachable) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "new_debug_unreachable"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
