# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rav1e
%global full_version 0.8.1
%global pkgname rav1e-0.8

Name:           rust-rav1e-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "rav1e"
License:        BSD-2-Clause
URL:            https://github.com/xiph/rav1e/
#!RemoteAsset:  sha256:43b6dd56e85d9483277cde964fd1bdb0428de4fec5ebba7540995639a21cb32b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aligned-vec-0.6/default) >= 0.6.4
Requires:       crate(arbitrary-1.0/default) >= 1.4.2
Requires:       crate(arg-enum-proc-macro-0.3/default) >= 0.3.4
Requires:       crate(arrayvec-0.7/default) >= 0.7.6
Requires:       crate(av-scenechange-0.14) >= 0.14.1
Requires:       crate(av1-grain-0.2/default) >= 0.2.5
Requires:       crate(bitstream-io-4.0/default) >= 4.10.0
Requires:       crate(built-0.8/default) >= 0.8.0
Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(interpolate-name-0.2/default) >= 0.2.4
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(libfuzzer-sys-0.4/default) >= 0.4.12
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(maybe-rayon-0.1) >= 0.1.1
Requires:       crate(new-debug-unreachable-1.0/default) >= 1.0.6
Requires:       crate(noop-proc-macro-0.3/default) >= 0.3.0
Requires:       crate(num-derive-0.4/default) >= 0.4.2
Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(paste-1.0/default) >= 1.0.15
Requires:       crate(profiling-1.0/default) >= 1.0.18
Requires:       crate(rand-0.9/default) >= 0.9.4
Requires:       crate(rand-chacha-0.9/default) >= 0.9.0
Requires:       crate(simd-helpers-0.1/default) >= 0.1.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(v-frame-0.3/default) >= 0.3.9
Provides:       crate(rav1e) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/bench)
Provides:       crate(%{pkgname}/check-asm)
Provides:       crate(%{pkgname}/quick-test)
Provides:       crate(%{pkgname}/unstable)

%description
Source code for takopackized Rust crate "rav1e"

%package     -n %{name}+aom-sys
Summary:        Fastest and safest AV1 encoder - feature "aom-sys" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(aom-sys-0.3/default) >= 0.3.3
Provides:       crate(%{pkgname}/aom-sys)
Provides:       crate(%{pkgname}/decode-test)

%description -n %{name}+aom-sys
This metapackage enables feature "aom-sys" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "decode_test" feature.

%package     -n %{name}+asm
Summary:        Fastest and safest AV1 encoder - feature "asm"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cc)
Requires:       crate(%{pkgname}/nasm-rs)
Provides:       crate(%{pkgname}/asm)

%description -n %{name}+asm
This metapackage enables feature "asm" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+av-metrics
Summary:        Fastest and safest AV1 encoder - feature "av-metrics"
Requires:       crate(%{pkgname})
Requires:       crate(av-metrics-0.9) >= 0.9.1
Provides:       crate(%{pkgname}/av-metrics)

%description -n %{name}+av-metrics
This metapackage enables feature "av-metrics" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+backtrace
Summary:        Fastest and safest AV1 encoder - feature "backtrace" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(backtrace-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/backtrace)
Provides:       crate(%{pkgname}/desync-finder)

%description -n %{name}+backtrace
This metapackage enables feature "backtrace" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "desync_finder" feature.

%package     -n %{name}+binaries
Summary:        Fastest and safest AV1 encoder - feature "binaries"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/av-metrics)
Requires:       crate(%{pkgname}/clap)
Requires:       crate(%{pkgname}/clap-complete)
Requires:       crate(%{pkgname}/console)
Requires:       crate(%{pkgname}/fern)
Requires:       crate(%{pkgname}/ivf)
Requires:       crate(%{pkgname}/nom)
Requires:       crate(%{pkgname}/scan-fmt)
Requires:       crate(%{pkgname}/y4m)
Provides:       crate(%{pkgname}/binaries)

%description -n %{name}+binaries
This metapackage enables feature "binaries" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+byteorder
Summary:        Fastest and safest AV1 encoder - feature "byteorder"
Requires:       crate(%{pkgname})
Requires:       crate(byteorder-1.0/default) >= 1.5.0
Provides:       crate(%{pkgname}/byteorder)

%description -n %{name}+byteorder
This metapackage enables feature "byteorder" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cc
Summary:        Fastest and safest AV1 encoder - feature "cc"
Requires:       crate(%{pkgname})
Requires:       crate(cc-1.0/default) >= 1.0.0
Requires:       crate(cc-1.0/parallel) >= 1.0.0
Provides:       crate(%{pkgname}/cc)

%description -n %{name}+cc
This metapackage enables feature "cc" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap
Summary:        Fastest and safest AV1 encoder - feature "clap"
Requires:       crate(%{pkgname})
Requires:       crate(clap-4.0/color) >= 4.5
Requires:       crate(clap-4.0/derive) >= 4.5
Requires:       crate(clap-4.0/std) >= 4.5
Requires:       crate(clap-4.0/wrap-help) >= 4.5
Provides:       crate(%{pkgname}/clap)

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap-complete
Summary:        Fastest and safest AV1 encoder - feature "clap_complete"
Requires:       crate(%{pkgname})
Requires:       crate(clap-complete-4.0/default) >= 4.5
Provides:       crate(%{pkgname}/clap-complete)

%description -n %{name}+clap-complete
This metapackage enables feature "clap_complete" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+console
Summary:        Fastest and safest AV1 encoder - feature "console"
Requires:       crate(%{pkgname})
Requires:       crate(console-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/console)

%description -n %{name}+console
This metapackage enables feature "console" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossbeam
Summary:        Fastest and safest AV1 encoder - feature "crossbeam" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(crossbeam-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/channel-api)
Provides:       crate(%{pkgname}/crossbeam)

%description -n %{name}+crossbeam
This metapackage enables feature "crossbeam" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "channel-api" feature.

%package     -n %{name}+dav1d-sys
Summary:        Fastest and safest AV1 encoder - feature "dav1d-sys" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(libdav1d-sys-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/dav1d-sys)
Provides:       crate(%{pkgname}/decode-test-dav1d)

%description -n %{name}+dav1d-sys
This metapackage enables feature "dav1d-sys" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "decode_test_dav1d" feature.

%package     -n %{name}+default
Summary:        Fastest and safest AV1 encoder - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/asm)
Requires:       crate(%{pkgname}/binaries)
Requires:       crate(%{pkgname}/git-version)
Requires:       crate(%{pkgname}/signal-support)
Requires:       crate(%{pkgname}/threading)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-lookahead-data
Summary:        Fastest and safest AV1 encoder - feature "dump_lookahead_data"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/byteorder)
Requires:       crate(%{pkgname}/image)
Provides:       crate(%{pkgname}/dump-lookahead-data)

%description -n %{name}+dump-lookahead-data
This metapackage enables feature "dump_lookahead_data" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fern
Summary:        Fastest and safest AV1 encoder - feature "fern"
Requires:       crate(%{pkgname})
Requires:       crate(fern-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/fern)

%description -n %{name}+fern
This metapackage enables feature "fern" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+git-version
Summary:        Fastest and safest AV1 encoder - feature "git_version"
Requires:       crate(%{pkgname})
Requires:       crate(built-0.8/git2) >= 0.8.0
Provides:       crate(%{pkgname}/git-version)

%description -n %{name}+git-version
This metapackage enables feature "git_version" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+image
Summary:        Fastest and safest AV1 encoder - feature "image"
Requires:       crate(%{pkgname})
Requires:       crate(image-0.25/png) >= 0.25.0
Provides:       crate(%{pkgname}/image)

%description -n %{name}+image
This metapackage enables feature "image" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ivf
Summary:        Fastest and safest AV1 encoder - feature "ivf" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(ivf-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/dump-ivf)
Provides:       crate(%{pkgname}/ivf)

%description -n %{name}+ivf
This metapackage enables feature "ivf" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dump_ivf" feature.

%package     -n %{name}+nasm-rs
Summary:        Fastest and safest AV1 encoder - feature "nasm-rs"
Requires:       crate(%{pkgname})
Requires:       crate(nasm-rs-0.3/default) >= 0.3.0
Requires:       crate(nasm-rs-0.3/parallel) >= 0.3.0
Provides:       crate(%{pkgname}/nasm-rs)

%description -n %{name}+nasm-rs
This metapackage enables feature "nasm-rs" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nom
Summary:        Fastest and safest AV1 encoder - feature "nom"
Requires:       crate(%{pkgname})
Requires:       crate(nom-8.0/default) >= 8.0.0
Provides:       crate(%{pkgname}/nom)

%description -n %{name}+nom
This metapackage enables feature "nom" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scan-fmt
Summary:        Fastest and safest AV1 encoder - feature "scan_fmt" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(scan-fmt-0.2) >= 0.2.6
Provides:       crate(%{pkgname}/capi)
Provides:       crate(%{pkgname}/scan-fmt)

%description -n %{name}+scan-fmt
This metapackage enables feature "scan_fmt" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "capi" feature.

%package     -n %{name}+serde
Summary:        Fastest and safest AV1 encoder - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-big-array
Summary:        Fastest and safest AV1 encoder - feature "serde-big-array"
Requires:       crate(%{pkgname})
Requires:       crate(serde-big-array-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname}/serde-big-array)

%description -n %{name}+serde-big-array
This metapackage enables feature "serde-big-array" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialize
Summary:        Fastest and safest AV1 encoder - feature "serialize"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/serde-big-array)
Requires:       crate(%{pkgname}/toml)
Requires:       crate(av1-grain-0.2/serialize) >= 0.2.5
Requires:       crate(v-frame-0.3/serialize) >= 0.3.9
Provides:       crate(%{pkgname}/serialize)

%description -n %{name}+serialize
This metapackage enables feature "serialize" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signal-hook
Summary:        Fastest and safest AV1 encoder - feature "signal-hook" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(signal-hook-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/signal-hook)
Provides:       crate(%{pkgname}/signal-support)

%description -n %{name}+signal-hook
This metapackage enables feature "signal-hook" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "signal_support" feature.

%package     -n %{name}+threading
Summary:        Fastest and safest AV1 encoder - feature "threading"
Requires:       crate(%{pkgname})
Requires:       crate(maybe-rayon-0.1/threads) >= 0.1.1
Provides:       crate(%{pkgname}/threading)

%description -n %{name}+threading
This metapackage enables feature "threading" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+toml
Summary:        Fastest and safest AV1 encoder - feature "toml"
Requires:       crate(%{pkgname})
Requires:       crate(toml-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/toml)

%description -n %{name}+toml
This metapackage enables feature "toml" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Fastest and safest AV1 encoder - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/tracing-chrome)
Requires:       crate(%{pkgname}/tracing-subscriber)
Requires:       crate(profiling-1.0/profile-with-tracing) >= 1.0.18
Requires:       crate(tracing-0.1/default) >= 0.1.40
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-chrome
Summary:        Fastest and safest AV1 encoder - feature "tracing-chrome"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-chrome-0.7/default) >= 0.7.1
Provides:       crate(%{pkgname}/tracing-chrome)

%description -n %{name}+tracing-chrome
This metapackage enables feature "tracing-chrome" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-subscriber
Summary:        Fastest and safest AV1 encoder - feature "tracing-subscriber"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.18
Provides:       crate(%{pkgname}/tracing-subscriber)

%description -n %{name}+tracing-subscriber
This metapackage enables feature "tracing-subscriber" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Fastest and safest AV1 encoder - feature "wasm-bindgen" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.121
Provides:       crate(%{pkgname}/wasm)
Provides:       crate(%{pkgname}/wasm-bindgen)

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "wasm" feature.

%package     -n %{name}+y4m
Summary:        Fastest and safest AV1 encoder - feature "y4m"
Requires:       crate(%{pkgname})
Requires:       crate(y4m-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/y4m)

%description -n %{name}+y4m
This metapackage enables feature "y4m" for the Rust rav1e crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
