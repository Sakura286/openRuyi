# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ravif
%global full_version 0.13.0
%global pkgname ravif-0.13

Name:           rust-ravif-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "ravif"
License:        BSD-3-Clause
URL:            https://lib.rs/crates/ravif
#!RemoteAsset:  sha256:e52310197d971b0f5be7fe6b57530dcd27beb35c1b013f29d66c1ad73fbbcc45
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(avif-serialize-0.8/default) >= 0.8.9
Requires:       crate(imgref-1.0/default) >= 1.12.1
Requires:       crate(loop9-0.1/default) >= 0.1.5
Requires:       crate(quick-error-2.0/default) >= 2.0.1
Requires:       crate(rav1e-0.8) >= 0.8.1
Requires:       crate(rav1e-0.8/wasm) >= 0.8.1
Requires:       crate(rgb-0.8) >= 0.8.53
Provides:       crate(ravif) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "ravif"

%package     -n %{name}+asm
Summary:        Rav1e-based pure Rust library for encoding images in AVIF format (powers the `cavif` tool) - feature "asm"
Requires:       crate(%{pkgname})
Requires:       crate(rav1e-0.8/asm) >= 0.8.1
Requires:       crate(rav1e-0.8/wasm) >= 0.8.1
Provides:       crate(%{pkgname}/asm)

%description -n %{name}+asm
This metapackage enables feature "asm" for the Rust ravif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rav1e-based pure Rust library for encoding images in AVIF format (powers the `cavif` tool) - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/asm)
Requires:       crate(%{pkgname}/threading)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ravif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+threading
Summary:        Rav1e-based pure Rust library for encoding images in AVIF format (powers the `cavif` tool) - feature "threading"
Requires:       crate(%{pkgname})
Requires:       crate(rav1e-0.8/threading) >= 0.8.1
Requires:       crate(rav1e-0.8/wasm) >= 0.8.1
Requires:       crate(rayon-1.0/default) >= 1.11.0
Provides:       crate(%{pkgname}/threading)

%description -n %{name}+threading
This metapackage enables feature "threading" for the Rust ravif crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
