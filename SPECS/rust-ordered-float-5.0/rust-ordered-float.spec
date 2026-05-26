# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ordered-float
%global full_version 5.3.0
%global pkgname ordered-float-5.0

Name:           rust-ordered-float-5.0
Version:        5.3.0
Release:        %autorelease
Summary:        Rust crate "ordered-float"
License:        MIT
URL:            https://github.com/reem/rust-ordered-float
#!RemoteAsset:  sha256:b7d950ca161dc355eaf28f82b11345ed76c6e1f6eb1f4f4479e0323b9e2fbd0e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2) >= 0.2.19
Provides:       crate(ordered-float) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "ordered-float"

%package     -n %{name}+arbitrary
Summary:        Wrappers for total ordering on floats - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+borsh
Summary:        Wrappers for total ordering on floats - feature "borsh"
Requires:       crate(%{pkgname})
Requires:       crate(borsh-1.0) >= 1.2.0
Provides:       crate(%{pkgname}/borsh)

%description -n %{name}+borsh
This metapackage enables feature "borsh" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Wrappers for total ordering on floats - feature "bytemuck"
Requires:       crate(%{pkgname})
Requires:       crate(bytemuck-1.0) >= 1.12.2
Provides:       crate(%{pkgname}/bytemuck)

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive-visitor
Summary:        Wrappers for total ordering on floats - feature "derive-visitor"
Requires:       crate(%{pkgname})
Requires:       crate(derive-visitor-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/derive-visitor)

%description -n %{name}+derive-visitor
This metapackage enables feature "derive-visitor" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        Wrappers for total ordering on floats - feature "libm"
Requires:       crate(%{pkgname})
Requires:       crate(num-traits-0.2/libm) >= 0.2.19
Provides:       crate(%{pkgname}/libm)

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-cmp
Summary:        Wrappers for total ordering on floats - feature "num-cmp"
Requires:       crate(%{pkgname})
Requires:       crate(num-cmp-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/num-cmp)

%description -n %{name}+num-cmp
This metapackage enables feature "num-cmp" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest
Summary:        Wrappers for total ordering on floats - feature "proptest"
Requires:       crate(%{pkgname})
Requires:       crate(proptest-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/proptest)

%description -n %{name}+proptest
This metapackage enables feature "proptest" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Wrappers for total ordering on floats - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8) >= 0.8.6
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+randtest
Summary:        Wrappers for total ordering on floats - feature "randtest"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8/std) >= 0.8.6
Requires:       crate(rand-0.8/std-rng) >= 0.8.6
Provides:       crate(%{pkgname}/randtest)

%description -n %{name}+randtest
This metapackage enables feature "randtest" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-08-16
Summary:        Wrappers for total ordering on floats - feature "rkyv_08_16"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.8) >= 0.8.0
Requires:       crate(rkyv-0.8/pointer-width-16) >= 0.8.0
Provides:       crate(%{pkgname}/rkyv-08-16)

%description -n %{name}+rkyv-08-16
This metapackage enables feature "rkyv_08_16" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-08-32
Summary:        Wrappers for total ordering on floats - feature "rkyv_08_32" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.8) >= 0.8.0
Requires:       crate(rkyv-0.8/pointer-width-32) >= 0.8.0
Provides:       crate(%{pkgname}/rkyv-08)
Provides:       crate(%{pkgname}/rkyv-08-32)

%description -n %{name}+rkyv-08-32
This metapackage enables feature "rkyv_08_32" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rkyv_08" feature.

%package     -n %{name}+rkyv-08-64
Summary:        Wrappers for total ordering on floats - feature "rkyv_08_64"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.8) >= 0.8.0
Requires:       crate(rkyv-0.8/pointer-width-64) >= 0.8.0
Provides:       crate(%{pkgname}/rkyv-08-64)

%description -n %{name}+rkyv-08-64
This metapackage enables feature "rkyv_08_64" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-08-ck
Summary:        Wrappers for total ordering on floats - feature "rkyv_08_ck"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.8) >= 0.8.0
Requires:       crate(rkyv-0.8/bytecheck) >= 0.8.0
Provides:       crate(%{pkgname}/rkyv-08-ck)

%description -n %{name}+rkyv-08-ck
This metapackage enables feature "rkyv_08_ck" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-16
Summary:        Wrappers for total ordering on floats - feature "rkyv_16"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7/rend) >= 0.7.41
Requires:       crate(rkyv-0.7/size-16) >= 0.7.41
Provides:       crate(%{pkgname}/rkyv-16)

%description -n %{name}+rkyv-16
This metapackage enables feature "rkyv_16" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-32
Summary:        Wrappers for total ordering on floats - feature "rkyv_32" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7/rend) >= 0.7.41
Requires:       crate(rkyv-0.7/size-32) >= 0.7.41
Provides:       crate(%{pkgname}/rkyv)
Provides:       crate(%{pkgname}/rkyv-32)

%description -n %{name}+rkyv-32
This metapackage enables feature "rkyv_32" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rkyv" feature.

%package     -n %{name}+rkyv-64
Summary:        Wrappers for total ordering on floats - feature "rkyv_64"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7/rend) >= 0.7.41
Requires:       crate(rkyv-0.7/size-64) >= 0.7.41
Provides:       crate(%{pkgname}/rkyv-64)

%description -n %{name}+rkyv-64
This metapackage enables feature "rkyv_64" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-ck
Summary:        Wrappers for total ordering on floats - feature "rkyv_ck"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7/rend) >= 0.7.41
Requires:       crate(rkyv-0.7/validation) >= 0.7.41
Provides:       crate(%{pkgname}/rkyv-ck)

%description -n %{name}+rkyv-ck
This metapackage enables feature "rkyv_ck" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars
Summary:        Wrappers for total ordering on floats - feature "schemars"
Requires:       crate(%{pkgname})
Requires:       crate(schemars-0.8/default) >= 0.8.8
Provides:       crate(%{pkgname}/schemars)

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Wrappers for total ordering on floats - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8/serde1) >= 0.8.6
Requires:       crate(serde-1.0) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+speedy
Summary:        Wrappers for total ordering on floats - feature "speedy"
Requires:       crate(%{pkgname})
Requires:       crate(speedy-0.8) >= 0.8.3
Provides:       crate(%{pkgname}/speedy)

%description -n %{name}+speedy
This metapackage enables feature "speedy" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Wrappers for total ordering on floats - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
