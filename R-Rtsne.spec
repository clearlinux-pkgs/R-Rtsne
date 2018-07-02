#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Rtsne
Version  : 0.13
Release  : 10
URL      : https://cran.r-project.org/src/contrib/Rtsne_0.13.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Rtsne_0.13.tar.gz
Summary  : T-Distributed Stochastic Neighbor Embedding using a Barnes-Hut
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-Rtsne-lib
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : clr-R-helpers

%description
[![CRAN version](http://www.r-pkg.org/badges/version/Rtsne)](https://cran.r-project.org/package=Rtsne/) [![Travis-CI Build Status](https://travis-ci.org/jkrijthe/Rtsne.png?branch=master)](https://travis-ci.org/jkrijthe/Rtsne) [![codecov.io](https://codecov.io/github/jkrijthe/Rtsne/coverage.svg?branch=master)](https://codecov.io/github/jkrijthe/Rtsne?branch=master) [![CRAN mirror downloads](http://cranlogs.r-pkg.org/badges/Rtsne)](https://cran.r-project.org/package=Rtsne/)

%package lib
Summary: lib components for the R-Rtsne package.
Group: Libraries

%description lib
lib components for the R-Rtsne package.


%prep
%setup -q -c -n Rtsne

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521242629

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521242629
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rtsne
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rtsne
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rtsne
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library Rtsne|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Rtsne/CITATION
/usr/lib64/R/library/Rtsne/DESCRIPTION
/usr/lib64/R/library/Rtsne/INDEX
/usr/lib64/R/library/Rtsne/LICENSE
/usr/lib64/R/library/Rtsne/Meta/Rd.rds
/usr/lib64/R/library/Rtsne/Meta/features.rds
/usr/lib64/R/library/Rtsne/Meta/hsearch.rds
/usr/lib64/R/library/Rtsne/Meta/links.rds
/usr/lib64/R/library/Rtsne/Meta/nsInfo.rds
/usr/lib64/R/library/Rtsne/Meta/package.rds
/usr/lib64/R/library/Rtsne/NAMESPACE
/usr/lib64/R/library/Rtsne/R/Rtsne
/usr/lib64/R/library/Rtsne/R/Rtsne.rdb
/usr/lib64/R/library/Rtsne/R/Rtsne.rdx
/usr/lib64/R/library/Rtsne/help/AnIndex
/usr/lib64/R/library/Rtsne/help/Rtsne.rdb
/usr/lib64/R/library/Rtsne/help/Rtsne.rdx
/usr/lib64/R/library/Rtsne/help/aliases.rds
/usr/lib64/R/library/Rtsne/help/paths.rds
/usr/lib64/R/library/Rtsne/html/00Index.html
/usr/lib64/R/library/Rtsne/html/R.css
/usr/lib64/R/library/Rtsne/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/Rtsne/libs/Rtsne.so
/usr/lib64/R/library/Rtsne/libs/Rtsne.so.avx2
/usr/lib64/R/library/Rtsne/libs/Rtsne.so.avx512
