module Days.Day03 where

import Data.Char (ord)

ctoi :: Char -> Int
ctoi = subtract (ord '0') . ord

maxJoltage :: Char -> (Int, Int) -> (Int, Int)
maxJoltage c xs =
  let x = ctoi c
   in (max (fst xs) (x * 10 + snd xs), max (snd xs) x)

solveLine :: String -> Int
solveLine = fst . liftA2 (foldr maxJoltage) ((,) 0 . ctoi . last) init

part1 :: String -> String
part1 = show . sum . fmap solveLine . lines
