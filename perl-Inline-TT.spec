%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pnam	TT
Summary:	Inline::TT perl module
Summary(pl):	Modu³ perla Inline::TT
Name:		perl-Inline-TT
Version:	0.01
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-Template-Toolkit >= 2.07
BuildRequires:	perl-Test-Simple >= 0.32
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::TT  - use TT BLOCK as Perl subs. Template-Toolkit is not just
a Templating Engine. It's a language. Inline::TT is a Inline plugin to
allow you to code your Perl subs in TT.
    
%description -l pl
Modu³ Inline::TT - pozwalaj±cy na u¿ywanie bloków TT jako procedur
Perla. Template-Toolkit to nie tylko mechanizm obs³uguj±cy wzorce - to
jêzyk. A Inline::TT pozwala na pisanie procedur Perla w jêzyku TT.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Inline/TT.pm
%{_mandir}/man3/*
