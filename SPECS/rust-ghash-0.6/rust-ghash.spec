# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ghash
%global full_version 0.6.0
%global pkgname ghash-0.6

Name:           rust-ghash-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "ghash"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/universal-hashes
#!RemoteAsset:  sha256:2eecf2d5dc9b66b732b97707a0210906b1d30523eb773193ab777c0c84b3e8d5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(polyval-0.7/default) >= 0.7.1
Requires:       crate(polyval-0.7/hazmat) >= 0.7.1
Provides:       crate(ghash) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "ghash"

%package     -n %{name}+zeroize
Summary:        Universal hash over GF(2^128) useful for constructing a Message Authentication Code (MAC), as in the AES-GCM authenticated encryption cipher - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(polyval-0.7/hazmat) >= 0.7.1
Requires:       crate(polyval-0.7/zeroize) >= 0.7.1
Requires:       crate(zeroize-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust ghash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
