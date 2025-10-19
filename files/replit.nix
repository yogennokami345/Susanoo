{ pkgs }:

pkgs.mkShell {
  deps = with pkgs; [
    python310Full
    (python310.withPackages (ps: with ps; [
      discord-py
      flask
    ]))
  ];
}

