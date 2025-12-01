module Days.Day01 where

rotToInt :: String -> Int
rotToInt ('L' : xs) = -(read xs :: Int)
rotToInt (_ : xs) = read xs
rotToInt "" = 0

part1 :: String -> String
part1 =
  (show :: Int -> String)
    . snd
    . foldl
      ( \xs x ->
          let fst' = (fst xs + x) `mod` 100
              snd' = snd xs + if fst' == 0 then 1 else 0
           in (fst', snd')
      )
      (50, 0)
    . fmap rotToInt
    . lines

part2 :: String -> String
part2 =
  (show :: Int -> String)
    . snd
    . foldl
      ( \xs x ->
          let fst' = (fst xs + x) `mod` 100
              snd' =
                snd xs
                  + if x >= 0
                    then (fst xs + x) `div` 100
                    else (((100 - fst xs) `mod` 100) + abs x) `div` 100
           in (fst', snd')
      )
      (50, 0)
    . fmap rotToInt
    . lines
