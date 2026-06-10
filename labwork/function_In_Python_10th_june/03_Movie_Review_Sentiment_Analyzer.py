# ==========================================================
# Movie Review Sentiment Analyzer
# ==========================================================
# Problem:
# Analyze movie reviews using functions.
#
# Functions:
# 1. count_sentiments(reviews)
# 2. most_common_word(reviews)
# 3. longest_review(reviews)
# 4. reviews_with_keyword(reviews, keyword)
# ==========================================================


# List containing movie reviews
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]


# ==========================================================
# Function 1: Count Sentiments
# Counts Excellent, Good, Average and Poor reviews
# ==========================================================
def count_sentiments(reviews):

    excellent_count = 0
    good_count = 0
    average_count = 0
    poor_count = 0

    for review in reviews:

        if "excellent" in review:
            excellent_count += 1

        elif "good" in review:
            good_count += 1

        elif "average" in review:
            average_count += 1

        elif "poor" in review:
            poor_count += 1

    return (
        excellent_count,
        good_count,
        average_count,
        poor_count
    )


# ==========================================================
# Function 2: Find Most Common Word
# Returns the word occurring maximum number of times
# ==========================================================
def most_common_word(reviews):

    word_frequency = {}

    # Create frequency dictionary
    for review in reviews:

        words = review.split()

        for word in words:

            if word in word_frequency:
                word_frequency[word] += 1

            else:
                word_frequency[word] = 1

    # Find word with highest frequency
    max_count = 0
    common_word = ""

    for word, frequency in word_frequency.items():

        if frequency > max_count:

            max_count = frequency
            common_word = word

    return common_word


# ==========================================================
# Function 3: Find Longest Review
# Returns review having maximum characters
# ==========================================================
def longest_review(reviews):

    longest = reviews[0]

    for review in reviews:

        if len(review) > len(longest):
            longest = review

    return longest


# ==========================================================
# Function 4: Display Reviews Containing Keyword
# ==========================================================
def reviews_with_keyword(reviews, keyword):

    print(f"\nReviews containing '{keyword}':")

    for review in reviews:

        if keyword.lower() in review.lower():
            print(review)


# ==========================================================
# Main Program
# ==========================================================

# Count sentiments
excellent, good, average, poor = count_sentiments(reviews)

print("Excellent Reviews:", excellent)
print("Good Reviews:", good)
print("Average Reviews:", average)
print("Poor Reviews:", poor)

print()

# Display most common word
print("Most Common Word:")
print(most_common_word(reviews))

print()

# Display longest review
print("Longest Review:")
print(longest_review(reviews))

print()

# Display reviews containing keyword
reviews_with_keyword(reviews, "excellent")
'''Sample Output

Excellent Reviews: 4
Good Reviews: 2
Average Reviews: 2
Poor Reviews: 2

Most Common Word:
excellent

Longest Review:
good cinematography

Reviews containing 'excellent':
excellent movie
excellent acting
excellent visuals
excellent climax

 '''