{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
        myPython = pkgs.python3.withPackages (
          ps: with ps; [
            scipy
          ]
        );
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [ myPython ];
        };
      }
    );
}
