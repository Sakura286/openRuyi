# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustcrypto-group
%global full_version 0.14.0-rc.1
%global pkgname rustcrypto-group-0.14.0-rc.1

Name:           rust-rustcrypto-group-0.14.0-rc.1
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "rustcrypto-group"
License:        MIT/Apache-2.0
URL:            https://github.com/RustCrypto/group
#!RemoteAsset:  sha256:369f9b61aa45933c062c9f6b5c3c50ab710687eca83dd3802653b140b43f85ed
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.10) >= 0.10.1
Requires:       crate(rustcrypto-ff-0.14.0-rc.1) >= 0.14.0-rc.1
Requires:       crate(subtle-2.0) >= 2.6.1
Provides:       crate(rustcrypto-group) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "rustcrypto-group"

%package     -n %{name}+memuse
Summary:        Elliptic curve group traits and utilities - feature "memuse"
Requires:       crate(%{pkgname})
Requires:       crate(memuse-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/memuse)

%description -n %{name}+memuse
This metapackage enables feature "memuse" for the Rust rustcrypto-group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Elliptic curve group traits and utilities - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust rustcrypto-group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-xorshift
Summary:        Elliptic curve group traits and utilities - feature "rand_xorshift"
Requires:       crate(%{pkgname})
Requires:       crate(rand-xorshift-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/rand-xorshift)

%description -n %{name}+rand-xorshift
This metapackage enables feature "rand_xorshift" for the Rust rustcrypto-group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tests
Summary:        Elliptic curve group traits and utilities - feature "tests"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/rand)
Requires:       crate(%{pkgname}/rand-xorshift)
Provides:       crate(%{pkgname}/tests)

%description -n %{name}+tests
This metapackage enables feature "tests" for the Rust rustcrypto-group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wnaf-memuse
Summary:        Elliptic curve group traits and utilities - feature "wnaf-memuse"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/memuse)
Provides:       crate(%{pkgname}/wnaf-memuse)

%description -n %{name}+wnaf-memuse
This metapackage enables feature "wnaf-memuse" for the Rust rustcrypto-group crate, by pulling in any additional dependencies needed by that feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
