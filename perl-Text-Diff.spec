#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Diff
Version  : 1.45
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Diff-1.45.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Diff-1.45.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-diff-perl/libtext-diff-perl_1.45-1.debian.tar.xz
Summary  : 'Perform diffs on files and record sets'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-2.0 MIT
Requires: perl-Text-Diff-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Algorithm::Diff)

%description
NAME
Text::Diff - Perform diffs on files and record sets
SYNOPSIS
use Text::Diff;

%package dev
Summary: dev components for the perl-Text-Diff package.
Group: Development
Provides: perl-Text-Diff-devel = %{version}-%{release}

%description dev
dev components for the perl-Text-Diff package.


%package license
Summary: license components for the perl-Text-Diff package.
Group: Default

%description license
license components for the perl-Text-Diff package.


%prep
%setup -q -n Text-Diff-1.45
cd ..
%setup -q -T -D -n Text-Diff-1.45 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Text-Diff-1.45/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Diff
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Diff/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Text-Diff/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1Text/Diff.pm
/usr/lib/perl5/vendor_perl/5.28.1Text/Diff/Config.pm
/usr/lib/perl5/vendor_perl/5.28.1Text/Diff/Table.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Diff.3
/usr/share/man/man3/Text::Diff::Config.3
/usr/share/man/man3/Text::Diff::Table.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Diff/LICENSE
/usr/share/package-licenses/perl-Text-Diff/deblicense_copyright
