{ pkgs, ... }:

{
  languages.python = {
    enable = true;
    package = pkgs.python314;
    uv.enable = true;
    # Wheels (numpy, matplotlib) need these on NixOS.
    libraries = [
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
    ];
  };
}
