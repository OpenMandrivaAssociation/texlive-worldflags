Name:		texlive-worldflags
Version:	68827
Release:	1
Summary:	Drawing flags with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/worldflags
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/worldflags.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/worldflags.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a package for drawing flags using TikZ. Currently the
national flags of all independent nations are included,
additionally some other flags of various organizations. A flag
can be drawn ... as a single TikZ-picture within ordinary text,
as a picture element within a TikZ-picture. The appearance of a
flag (size, frame etc.) can be adapted using optional
parameters.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/worldflags
%doc %{_texmfdistdir}/doc/latex/worldflags

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
