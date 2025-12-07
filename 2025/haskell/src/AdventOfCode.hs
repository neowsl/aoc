module AdventOfCode (solve) where

import Days.Day01
import Days.Day02
import Days.Day03
import Days.Day06

solve :: Int -> Int -> String -> String
solve day part
  | day == 1 && part == 1 = Days.Day01.part1
  | day == 1 && part == 2 = Days.Day01.part2
  | day == 2 && part == 1 = Days.Day02.part1
  | day == 2 && part == 2 = Days.Day02.part2
  | day == 3 && part == 1 = Days.Day03.part1
  | day == 6 && part == 1 = Days.Day06.part1
  | otherwise = error
