# Copyright 2013-2014 The Rust Project Developers. See the COPYRIGHT
# file at the top-level directory of this distribution and at
# http://rust-lang.org/COPYRIGHT.
#
# Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
# http://www.apache.org/licenses/LICENSE-2.0> or the MIT license
# <LICENSE-MIT or http://opensource.org/licenses/MIT>, at your
# option. This file may not be copied, modified, or distributed
# except according to those terms.

license1 = """// Copyright """
license2 = """ The Rust Project Developers. See the COPYRIGHT
// file at the top-level directory of this distribution and at
// http://rust-lang.org/COPYRIGHT.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// http://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or http://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.
"""

license3 = """# Copyright """
license4 = """ The Rust Project Developers. See the COPYRIGHT
# file at the top-level directory of this distribution and at
# http://rust-lang.org/COPYRIGHT.
#
# Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
# http://www.apache.org/licenses/LICENSE-2.0> or the MIT license
# <LICENSE-MIT or http://opensource.org/licenses/MIT>, at your
# option. This file may not be copied, modified, or distributed
# except according to those terms.
"""

exceptions = [
    "rt/rust_android_dummy.cpp", # BSD, chromium
    "rt/rust_android_dummy.h", # BSD, chromium
    "rt/isaac/randport.cpp", # public domain
    "rt/isaac/rand.h", # public domain
    "rt/isaac/standard.h", # public domain
    "libstd/sync/mpsc/mpsc_queue.rs", # BSD
    "libstd/sync/mpsc/spsc_queue.rs", # BSD
    "test/bench/shootout-binarytrees.rs", # BSD
    "test/bench/shootout-chameneos-redux.rs", # BSD
    "test/bench/shootout-fannkuch-redux.rs", # BSD
    "test/bench/shootout-fasta.rs", # BSD
    "test/bench/shootout-fasta-redux.rs", # BSD
    "test/bench/shootout-k-nucleotide.rs", # BSD
    "test/bench/shootout-mandelbrot.rs", # BSD
    "test/bench/shootout-meteor.rs", # BSD
    "test/bench/shootout-nbody.rs", # BSD
    "test/bench/shootout-regex-dna.rs", # BSD
    "test/bench/shootout-reverse-complement.rs", # BSD
    "test/bench/shootout-spectralnorm.rs", # BSD
    "test/bench/shootout-threadring.rs", # BSD
]

def check_license(name, contents):
    # Whitelist check
    for exception in exceptions:
        if name.endswith(exception):
            return True

    # Xfail check
    firstlineish = contents[:100]
    if firstlineish.find("ignore-license") != -1:
        return True

    # License check
    boilerplate = contents[:500]
    if (boilerplate.find(license1) == -1 or boilerplate.find(license2) == -1) and \
       (boilerplate.find(license3) == -1 or boilerplate.find(license4) == -1):
        return False
    return True
