defmodule AOC2024 do
  def main do
    day =
      IO.gets("Enter day: ")
      |> String.trim()
      |> String.pad_leading(2, "0")

    part =
      IO.gets("Enter part: ")
      |> String.trim()

    input =
      File.read!("../input/day#{day}.txt")
      |> String.trim()

    module = :"Elixir.Days.Day#{day}"
    function = :"part#{part}"

    start = Time.utc_now()

    ans = apply(module, function, [input])

    elapsed = Time.utc_now() |> Time.diff(start, :microsecond)

    IO.puts("")
    IO.puts(ans)
    IO.puts("")
    IO.puts("Executed in #{elapsed / 1000}ms")
  end
end
