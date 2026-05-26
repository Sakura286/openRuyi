# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name p384
%global full_version 0.14.0-rc.7
%global pkgname p384-0.14.0-rc.7

Name:           rust-p384-0.14.0-rc.7
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "p384"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/p384
#!RemoteAsset:  sha256:8c91df688211f5957dbe2ab599dcbcaade8d6d3cdc15c5b350d350d7d07ce423
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(fiat-crypto-0.3) >= 0.3.0
Provides:       crate(p384) = %{version}
Provides:       crate(%{pkgname})

%description
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
Source code for takopackized Rust crate "p384"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(ecdsa-0.17.0-rc.16/alloc) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(elliptic-curve-0.14.0-rc.28/alloc) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(primeorder-0.14.0-rc.7/alloc) >= 0.14.0-rc.7
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "alloc" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arithmetic
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "arithmetic" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(elliptic-curve-0.14.0-rc.28/arithmetic) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/digest) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(primefield-0.14.0-rc.7/default) >= 0.14.0-rc.7
Requires:       crate(primeorder-0.14.0-rc.7/default) >= 0.14.0-rc.7
Provides:       crate(%{pkgname}/arithmetic)
Provides:       crate(%{pkgname}/expose-field)

%description -n %{name}+arithmetic
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "arithmetic" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "expose-field" feature.

%package     -n %{name}+bits
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "bits"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(elliptic-curve-0.14.0-rc.28/bits) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/bits)

%description -n %{name}+bits
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "bits" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/ecdsa)
Requires:       crate(%{pkgname}/pem)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "default" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "digest"
Requires:       crate(%{pkgname})
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/digest) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/hazmat) >= 0.17.0-rc.16
Provides:       crate(%{pkgname}/digest)

%description -n %{name}+digest
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "digest" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdh
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "ecdh"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(elliptic-curve-0.14.0-rc.28/ecdh) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/ecdh)

%description -n %{name}+ecdh
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "ecdh" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "ecdsa"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/sha384)
Requires:       crate(ecdsa-0.17.0-rc.16/algorithm) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Provides:       crate(%{pkgname}/ecdsa)

%description -n %{name}+ecdsa
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "ecdsa" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa-core
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "ecdsa-core"
Requires:       crate(%{pkgname})
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Provides:       crate(%{pkgname}/ecdsa-core)

%description -n %{name}+ecdsa-core
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "ecdsa-core" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/getrandom) >= 0.17.0-rc.16
Requires:       crate(elliptic-curve-0.14.0-rc.28/getrandom) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "getrandom" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+group-digest
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "group-digest" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/hash2curve)
Requires:       crate(%{pkgname}/sha2)
Provides:       crate(%{pkgname}/group-digest)
Provides:       crate(%{pkgname}/oprf)

%description -n %{name}+group-digest
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "group-digest" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "oprf" feature.

%package     -n %{name}+hash2curve
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "hash2curve"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(hash2curve-0.14.0-rc.10/default) >= 0.14.0-rc.10
Requires:       crate(primeorder-0.14.0-rc.7/hash2curve) >= 0.14.0-rc.7
Provides:       crate(%{pkgname}/hash2curve)

%description -n %{name}+hash2curve
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "hash2curve" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hex-literal
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "hex-literal" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(hex-literal-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/hex-literal)
Provides:       crate(%{pkgname}/test-vectors)

%description -n %{name}+hex-literal
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "hex-literal" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "test-vectors" feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "pem"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pkcs8)
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/pem) >= 0.17.0-rc.16
Requires:       crate(elliptic-curve-0.14.0-rc.28/pem) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/pem)

%description -n %{name}+pem
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "pem" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "pkcs8"
Requires:       crate(%{pkgname})
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/pkcs8) >= 0.17.0-rc.16
Requires:       crate(elliptic-curve-0.14.0-rc.28/pkcs8) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/pkcs8)

%description -n %{name}+pkcs8
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "pkcs8" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serdect)
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/serde) >= 0.17.0-rc.16
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/serde) >= 0.14.0-rc.28
Requires:       crate(primeorder-0.14.0-rc.7/serde) >= 0.14.0-rc.7
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "serde" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serdect
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "serdect"
Requires:       crate(%{pkgname})
Requires:       crate(serdect-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/serdect)

%description -n %{name}+serdect
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "serdect" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "sha2"
Requires:       crate(%{pkgname})
Requires:       crate(sha2-0.11) >= 0.11.0
Provides:       crate(%{pkgname}/sha2)

%description -n %{name}+sha2
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "sha2" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha384
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "sha384"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/digest)
Requires:       crate(%{pkgname}/sha2)
Provides:       crate(%{pkgname}/sha384)

%description -n %{name}+sha384
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "sha384" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/getrandom)
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/std) >= 0.17.0-rc.16
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/std) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "std" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
