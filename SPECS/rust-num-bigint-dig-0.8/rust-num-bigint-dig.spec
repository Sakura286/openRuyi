# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-bigint-dig
%global full_version 0.8.6
%global pkgname num-bigint-dig-0.8

Name:           rust-num-bigint-dig-0.8
Version:        0.8.6
Release:        %autorelease
Summary:        Rust crate "num-bigint-dig"
License:        MIT/Apache-2.0
URL:            https://github.com/dignifiedquire/num-bigint
#!RemoteAsset:  sha256:e661dda6640fad38e827a6d4a310ff4763082116fe217f279885c97f511bb0b7
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1.0/spin-no-std) >= 1.5.0
Requires:       crate(libm-0.2/default) >= 0.2.16
Requires:       crate(num-integer-0.1/i128) >= 0.1.46
Requires:       crate(num-iter-0.1) >= 0.1.45
Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Requires:       crate(smallvec-1.0) >= 1.15.1
Provides:       crate(num-bigint-dig) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/i128)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/u64-digit)

%description
Source code for takopackized Rust crate "num-bigint-dig"

%package     -n %{name}+arbitrary
Summary:        Big integer implementation for Rust - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Big integer implementation for Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/u64-digit)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fuzz
Summary:        Big integer implementation for Rust - feature "fuzz"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arbitrary)
Requires:       crate(smallvec-1.0/arbitrary) >= 1.15.1
Provides:       crate(%{pkgname}/fuzz)

%description -n %{name}+fuzz
This metapackage enables feature "fuzz" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prime
Summary:        Big integer implementation for Rust - feature "prime"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8/std-rng) >= 0.8.6
Provides:       crate(%{pkgname}/prime)

%description -n %{name}+prime
This metapackage enables feature "prime" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Big integer implementation for Rust - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8) >= 0.8.6
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Big integer implementation for Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Big integer implementation for Rust - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(num-integer-0.1/i128) >= 0.1.46
Requires:       crate(num-integer-0.1/std) >= 0.1.46
Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(rand-0.8/std) >= 0.8.6
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Requires:       crate(serde-1.0/std) >= 1.0.228
Requires:       crate(smallvec-1.0/write) >= 1.15.1
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Big integer implementation for Rust - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.5
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
