%global tl_name worldflags
%global tl_revision 68827

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Drawing flags with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/worldflags
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/worldflags.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/worldflags.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a package for drawing flags using TikZ. Currently the national
flags of all independent nations are included, additionally some other
flags of various organizations. A flag can be drawn ... as a single
TikZ-picture within ordinary text, as a picture element within a TikZ-
picture. The appearance of a flag (size, frame etc.) can be adapted
using optional parameters.

