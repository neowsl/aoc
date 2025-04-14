defmodule Days.Day01 do
  def part1(input) do
    input
    |> String.split("\n")
    |> Enum.map(fn
      x ->
        x
        |> String.split("   ")
        |> Enum.map(&String.to_integer/1)
    end)
    |> List.zip()
    |> Enum.map(fn
      x ->
        x
        |> Tuple.to_list()
        |> Enum.sort()
    end)
    |> Enum.zip_with(fn [x, y] -> abs(x - y) end)
    |> Enum.sum()
    |> Integer.to_string()
  end
end
