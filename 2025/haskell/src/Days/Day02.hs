module Days.Day02 where

import Data.List.Split (splitOn)

isInvalid :: String -> Bool
isInvalid xs =
  even (length xs)
    && take (length xs `div` 2) xs == drop (length xs `div` 2) xs

findInvalid :: String -> [Int]
findInvalid xs =
  case fmap (read :: String -> Int) (splitOn "-" xs) of
    [low, high] -> filter (isInvalid . show) [low .. high]
    _ -> []

part1 :: String -> String
part1 = show . sum . concatMap findInvalid . splitOn ","

repeatedN :: String -> Int -> Bool
repeatedN xs n
  | length xs `mod` n /= 0 = False
  | n == 2 = isInvalid xs
  | otherwise =
      let m = length xs `div` n
       in isInvalid (take (m * 2) xs) && repeatedN (drop m xs) (n - 1)

isInvalid2 :: String -> Bool
isInvalid2 xs =
  any (repeatedN xs) [2 .. length xs]

findInvalid2 :: String -> [Int]
findInvalid2 xs =
  case fmap (read :: String -> Int) (splitOn "-" xs) of
    [low, high] -> filter (isInvalid2 . show) [low .. high]
    _ -> []

part2 :: String -> String
part2 = show . sum . concatMap findInvalid2 . splitOn ","
