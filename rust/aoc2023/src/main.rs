use phf::phf_map;
use regex::Regex;
use std::fs;

const DIGIT_VALUES: phf::Map<&str, u32> = phf_map! {
    "one" => 1,
    "two" => 2,
    "three" => 3,
    "four" => 4,
    "five" => 5,
    "six" => 6,
    "seven" => 7,
    "eight" => 8,
    "nine" => 9,
};
static DIGIT_PATTERN: &str = "([0-9]|one|two|three|four|five|six|seven|eight|nine)";

fn main() {
    println!("Welcome to AoC2023");
    {
        println!("=================== DAY 01 =================");
        let input: String = fs::read_to_string("data/day01.txt").unwrap();
        let ans: u32 = input.lines().map(cv).sum();
        println!("Part 1: {}", ans);
        let ans: u32 = input.lines().map(cav).sum();
        println!("Part 2: {}", ans);
    }
}

fn cv(s: &str) -> u32 {
    let fc = s.chars().find(char::is_ascii_digit).unwrap();
    let rc = s.chars().rev().find(char::is_ascii_digit).unwrap();
    let fd = fc.to_digit(10).unwrap();
    let rd = rc.to_digit(10).unwrap();
    10 * fd + rd
}

fn cav(s: &str) -> u32 {
    let re = Regex::new(DIGIT_PATTERN).unwrap();
    let fv = re.find_iter(s).next().unwrap().as_str();
    let rv = re.find_iter(s).last().unwrap().as_str();
    let fd = fv
        .parse::<u32>()
        .unwrap_or_else(|_| *DIGIT_VALUES.get(fv).unwrap());
    let rd = rv
        .parse::<u32>()
        .unwrap_or_else(|_| *DIGIT_VALUES.get(rv).unwrap());
    // if fd == rd {
    //     println!("Same: {} for {}", fd, s);
    // }
    10 * fd + rd
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;
    use regex::Regex;
    use std::{collections::HashMap, error::Error, fs};

    #[test]
    fn can_find_digit() {
        // given a string, find the first character in it that is a digit
        let s = "a1b2c3d4e5f";
        let mut f = s.chars().skip_while(|e| !e.is_ascii_digit());
        assert_eq!(Some('1'), f.next());
    }

    #[test]
    fn can_find_reverse_digit() {
        // given a string find the first character from the end that is a digit
        let s = "a1b2c3d4e5f";
        let mut f = s.chars().rev().skip_while(|e| !e.is_ascii_digit());
        assert_eq!(Some('5'), f.next());
    }

    #[test]
    fn can_find_calib_value() {
        let s = "a1b2c3d4e5f";
        let ans = cv(s);
        assert_eq!(15, ans);
    }

    #[test]
    fn can_sum_calib_values() {
        let s = indoc! { "
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
    "};
        let f: u32 = s.lines().map(cv).sum();
        assert_eq!(142, f);
    }

    #[test]
    fn solve_sum_calib_values() -> Result<(), Box<dyn Error>> {
        let input: String = fs::read_to_string("data/day01.txt")?;
        let ans: u32 = input.lines().map(cv).sum();
        assert_eq!(53974, ans);
        Ok(())
    }

    #[test]
    fn can_find_alphanum_digit() -> Result<(), Box<dyn Error>> {
        let s = "eightwothree";
        let re = Regex::new("([0-9]|eight)").unwrap();
        let mut digit_values = HashMap::new();
        digit_values.insert("eight", 8u32);
        let f = re.find_iter(s).next().unwrap().as_str();
        let ans: u32 = *digit_values.get(f).unwrap();
        assert_eq!(8, ans);
        Ok(())
    }

    #[test]
    fn can_find_reverse_alphanum_digit() -> Result<(), Box<dyn Error>> {
        let s = "eightwothree";
        let re = Regex::new("([0-9]|eight|three)").unwrap();
        let mut digit_values = HashMap::new();
        digit_values.insert("eight", 8u32);
        digit_values.insert("three", 3u32);
        let f = re.find_iter(s).last().unwrap().as_str();
        let ans: u32 = *digit_values.get(f).unwrap();
        assert_eq!(3, ans);
        Ok(())
    }

    #[test]
    fn can_find_alphanum_calib_value() -> Result<(), Box<dyn Error>> {
        let s = "eightwothree";
        let digit_values = HashMap::from([
            ("one", 1),
            ("two", 2),
            ("three", 3),
            ("four", 4),
            ("five", 5),
            ("eight", 8),
        ]);
        let re = Regex::new("([0-9]|one|two|three|eight)")?;
        let fv = re.find_iter(s).next().ok_or("Error")?.as_str();
        let rv = re.find_iter(s).last().unwrap().as_str();
        let fd: u32 = *digit_values.get(fv).unwrap();
        let rd: u32 = *digit_values.get(rv).unwrap();
        let ans = 10 * fd + rd;
        assert_eq!(83, ans);
        Ok(())
    }
    #[test]
    fn can_sum_alphanum_calib_value() {
        let s = indoc! {"
            two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen
        "};
        let ans: u32 = s.lines().map(cav).sum();
        assert_eq!(281, ans);
    }

    #[test]
    fn can_detect_all_valid_digits() {
        let re = Regex::new(DIGIT_PATTERN).unwrap();
        for i in 0..=9 {
            let s = i.to_string();
            let m = re
                .find_iter(&s)
                .next()
                .unwrap()
                .as_str()
                .parse::<i32>()
                .unwrap();
            assert_eq!(i, m);
        }
        for &k in DIGIT_VALUES.keys() {
            let m = re.find_iter(k).next().unwrap().as_str();
            // let v = *DIGIT_VALUES.get(k).unwrap();
            assert_eq!(k, m);
        }
    }

    #[test]
    fn solve_sum_alphanum_calib_values() -> Result<(), Box<dyn Error>> {
        let input: String = fs::read_to_string("data/day01.txt")?;
        let ans: u32 = input.lines().map(cav).sum();
        assert_eq!(52840, ans);
        Ok(())
    }
}
