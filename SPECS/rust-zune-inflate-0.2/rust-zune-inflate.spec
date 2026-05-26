# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zune-inflate
%global full_version 0.2.54
%global pkgname zune-inflate-0.2

Name:           rust-zune-inflate-0.2
Version:        0.2.54
Release:        %autorelease
Summary:        Rust crate "zune-inflate"
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://github.com/etemesi254/zune-image/tree/main/zune-inflate
#!RemoteAsset:  sha256:73ab332fe2f6680068f3582b16a24f90ad7096d5d39b974d1c0aff0125116f02
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(zune-inflate) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/gzip)

%description
Source code for takopackized Rust crate "zune-inflate"

%package     -n %{name}+default
Summary:        Heavily optimized deflate decompressor in Pure Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gzip)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/zlib)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zune-inflate crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simd-adler32
Summary:        Heavily optimized deflate decompressor in Pure Rust - feature "simd-adler32" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(simd-adler32-0.3) >= 0.3.9
Provides:       crate(%{pkgname}/simd-adler32)
Provides:       crate(%{pkgname}/zlib)

%description -n %{name}+simd-adler32
This metapackage enables feature "simd-adler32" for the Rust zune-inflate crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "zlib" feature.

%package     -n %{name}+std
Summary:        Heavily optimized deflate decompressor in Pure Rust - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(simd-adler32-0.3/std) >= 0.3.9
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust zune-inflate crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
