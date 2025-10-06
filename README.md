# courseFiltering
This implementation focuses on the core concept of finding courses that allign with the user's needs with both manual and AI-assisted searching.

<br>
<br>

**Task 1: Augment the design of a concept**

<br>


**ORIGINAL Concept** CourseFiltering [Course]

**Purpose**\
Enables users to efficiently locate courses relevant to their academic goals by narrowing down a large collection into a manageable set based on categories.

**Principle**\
Each class begins with a set of system assigned tags, and the user begins with a list of all available classes. The user selects one or more tags, and the filter produces a list of courses that only includes classes matching all selected tags. The user can then add or remove tags and get a new list of courses that only includes classes matching all selected tags. The user can then clear the filters to remove all active tags.

**State**
  - A set of courses with
    - A set of tags
- A set of tags with
  - An Id String
  - A category String
- A set of Active tags
- A set of Filtered courses

**Actions**
  - AddTag (t: tag)
    - **effects** adds tag to the active set and updates to ensure classes matching all selected tags are in set of filtered courses

  - RemoveTag (t: tag)
    - **effects** removes tag from the active set of tags and updates to ensure classes matching all selected tags are in set of filtered courses
      
  - ClearTags()
    - **effects** resets filter and clears the tags in the Active set of tags and clears the courses in the set of filtered courses

<br>
<br>

**AI AUGMENTED Concept CourseFiltering [Course]**

**Purpose**\
Enables users to efficiently locate courses relevant to their academic goals by narrowing down a large collection into a manageable set based on categories.

**Principle**\
Each class begins with a set of system assigned tags, and the user begins with a list of all available classes. The user selects one or more tags, and the filter produces a list of courses that only includes classes matching all selected tags. The user can then add or remove tags and get a new list of courses that only includes classes matching all selected tags. The user can then clear the filters to remove all active tags. In addition to manual filtering, the user may select a course and invoke AI to suggest alternative courses that share overlapping tags.

**State**
  - A set of courses with
    - A set of tags
  - A set of tags with
    - An id String
    - A category String
- A set of Active tags
- A set of Filtered courses
- A set of Suggested courses

**Actions**
  - AddTag (t: tag)
    - **effects** adds tag to the active set and updates to ensure classes matching all selected tags are in set of filtered courses
  - RemoveTag (t: tag)
    - **effects** removes tag from the active set of tags and updates to ensure classes matching all selected tags are in set of filtered courses
- ClearTags()
  - **effects** resets filter and clears the tags in the Active set of tags and clears the courses in the set of filtered courses
- suggestAlternatives (c : course)
  - **requires** that course to have associated tags
  - **effects** produces a set of suggested courses that share overlapping tags with the inputted course and updates Suggested courses to store these suggested courses

<br>
<br>
<br>

**Task 2: Design the user interaction**

<br>

![UI Sketch Page 1]([assignments/Images/IMG_0286.jpg](https://github.com/mg126e/61040-portfolio/blob/6cfb35c517c23a1ed032da9dc79b077425afff2e/assignments/Images/IMG_0286.jpg))
![UI Sketch Page 2]([Images/IMG_0285.jpg](https://github.com/mg126e/61040-portfolio/blob/6cfb35c517c23a1ed032da9dc79b077425afff2e/assignments/Images/IMG_0286.jpg))

<br>

**User Journey**

A Wellesley student navigates to the filter drop down next to the search bar and selects “History” for the department and “200” for the level. Hitting enter, the app displays a filtered list of courses, reducing the overwhelming set to a manageable number relevant to their major.

The student clicks on a course to view the professor’s rating and the distribution requirements the course satisfies (page 2). Liking the course, they click it to add it to their schedule. After reviewing their schedule, they add three more courses, leaving a full load of four. As a freshman, they worry about not getting into their preferred history class. They click on the class in their schedule (page 1), and look at the pop up (page 2) where the AI sidebar suggests backup options that fit their requirements and time slots. They add one as an alternative, feeling more confident that they’ll have a solid schedule even if their first choice fills up.

**Task 3: Implement your concept**
[Augmented Concept](courseFiltering.ts)
[Driver with Test cases](courseFiltering_tests.ts)
[Concpet Specification](couseFiltering.spec)

Implementation details below based on template README:

<br>
<br>

## Concept: Course Filtering

**Purpose**: Enables users to efficiently locate courses relevant to their academic goals by narrowing down a large collection into a manageable set based on categories. 
**Principle**: Each class begins with a set of system assigned tags, and the user begins with 
a list of all available classes. The user selects one or more tags, and the filter 
produces a list of courses that only includes classes matching all selected tags. 
The user can then add or remove tags and get a new list of courses that only includes 
classes matching all selected tags. The user can then clear the filters to remove all active tags. 
In addition to manual filtering, the user may select a course and invoke AI to suggest 
alternative courses that share overlapping tags.

### Core State
- **Courses**: set of tags and attributes like title and professor
- **Tags**: set of categories with names and ids
- **A set of Active tags**: a set of tags that the user selected
- **A set of Filtered courses**: a set of courses that align with the selected tags
- **A set of Suggested courses**: a set of courses that Gemini has suggested based on a user selected course

### Core Actions
- `AddTag (t: Tag)`
- `RemoveTag (t: Tag)`
- `ClearTags()`
- `suggestAlternatives (courseToSuggest : Course, llm : GeminiLLM, variant : "base" or "timeFocused" or "topicFocused")` - AI-assisted course suggestion with hardwired preferences



## Prerequisites

- **Node.js** (version 14 or higher)
- **TypeScript** 
- **Google Gemini API Key**


### 3. To run the Application

**Run all test cases:**
```bash
npm start
```

**Run specific test cases:**
```bash
npm run manual    # Manual filtering only
npm run llm       # LLM-assisted suggestions only
npm run mixed     # Mixed manual filtering + LLM course suggestions
```

## File Structure

```
CourseFiltering/
├── package.json              # Dependencies and scripts
├── tsconfig.json             # TypeScript configuration
├── config.json               # Your Gemini API key
├── courseFiltering.ts        # Course Filtering class implementation and core type definitions
├── gemini-llm.ts             # LLM integration
├── courseFiltering_tests.ts  # Test cases and examples
├── dist/                     # Compiled JavaScript output
└── README.md                 # This file
```

## Test Cases


### Part one Manual

#### 1 Adding and Removing a single Tag
Demonstrates manually adding and removing a single tag:

```typescript
const rawCourses: Course[] = coursesData as Course[];
const taggedCourses: Course[] = autoTagCourses(rawCourses);const courseFilter = new CourseFiltering(taggedCourses);

const historyTag: Tag = { id: "HIST", category: "Department" };
courseFilter.addTag(historyTag);

courseFilter.removeTag(historyTag);

```

#### 2 Adding and Removing multiple Tags
Demonstrates manually adding and removing multiple tags:

```typescript
const rawCourses: Course[] = coursesData as Course[];
const taggedCourses: Course[] = autoTagCourses(rawCourses);const courseFilter = new CourseFiltering(taggedCourses);

const historyTag: Tag = { id: "HIST", category: "Department" };
const profTag: Tag = { id: "Guy Rogers", category: "Professor" };
courseFilter.addTag(historyTag);
courseFilter.addTag(profTag);

courseFilter.clearTags();
```


### Part 2 LLM-Assisted Suggestions

#### 1. Base
Shows Ai suggested courses with a hardwired preference for no prioritization of one quality over another:

```typescript
const courseToSuggest = taggedCourses[226];
const suggestions = await courseFilter.suggestAlternatives(courseToSuggest, llm, "base");
```

My approach in this test was to evaluate how the AI performed with a neutral, general prompt that simply asked for courses “most similar in topic or content.” The LLM produced several suggestions, but many came from unrelated contexts, such as matching a course in english with a course in Chinese. This showed that without explicit guidance, the AI tended to rely on superficial or random overlaps in wording rather than meaningful academic similarity. While the results demonstrated that the base prompt can produce syntactically valid suggestions, it lacked consistent relevance. The main issue remaining is that the model needs clearer constraints to anchor similarity around shared tags or academic categories.

#### 2. Meeting Time
Shows Ai suggested courses with hardwired preference for prioritization of similar meeting times:

```typescript
const courseToSuggest = taggedCourses[226];
const suggestions = await courseFilter.suggestAlternatives(courseToSuggest, llm, "timeFocused");
```

For this variant, I modified the prompt to emphasize scheduling similarity, asking the AI to find courses that met at the same time and the same days. This approach worked in that the AI successfully returned courses that fit the same time window, demonstrating that it could reason about temporal patterns when provided with that context. However, several of the recommended courses were unrelated in subject matter—often pairing classes from different departments. This revealed a tradeoff between practical scheduling alignment and thematic relevance. The issue that remains is how to balance both dimensions in a single reasoning step, so that time alignment doesn’t overshadow academic similarity.

#### 3. Topic
Shows Ai suggested courses with hardwired preference for prioritization of similar topics:

```typescript
const courseToSuggest = taggedCourses[226];
const suggestions = await courseFilter.suggestAlternatives(courseToSuggest, llm, "topicFocused");
```
In this version, I asked the LLM to prioritize conceptual and thematic overlap, directing it to focus on shared keywords or course topics. This produced the most academically appropriate alternatives, as the AI selected courses that clearly connected by theme or subject area. However, some suggested courses were scheduled at completely different times, which would make them impractical as alternatives in a real scheduling scenario. This suggests that while topic-driven reasoning improves academic alignment, it ignores logistical considerations.


## Sample Output for Part 1

```
Active tags: [
  { id: 'HIST', category: 'Department' },
  { id: 'Guy Rogers', category: 'Professor' }
]

Filtered courses: [
  {
    course_code: 'HIST 200',
    section: '01',
    title: 'Roots of the Western Tradition',
    professor: 'Guy Rogers',
    meeting_time: 'TF - 12:45 PM - 2:00 PM',
    current_enrollment: 14,
    seats_available: 11,
    seats_total: 25,
    distribution: null,
  },
  {
    course_code: 'HIST 325',
    section: '01',
    title: '"Veni; Vidi; Vici":  The Life and Times of C. Iulius Caesar',
    professor: 'Guy Rogers',
    meeting_time: 'W - 6:30 PM - 9:10 PM',
    current_enrollment: 14,
    seats_available: 11,
    seats_total: 25,
    distribution: 'HS',
  }
]
```

## Sample Output for Part 2
```
Suggested Alternatives: [
  'Introduction to Classical Chinese (CHIN 310) (MR - 3:45 PM - 5:00 PM)',
  'Japanese Literature from Myth to Manga (in English) (JPN 251) (MR - 11:20 AM - 12:35 PM)',
  'Eileen Chang (in English) (CHIN 381) (W - 3:30 PM - 6:10 PM)'
]
```


## Validators
During testing, I identified three plausible issues in the AI’s output:
- The model sometimes “hallucinates” non-existent courses, so I added a validator that checks all returned course codes the known dataset and ensures that the course codes and course titles match.
- It can occasionally return duplicates, so I added a validator that checks for duplicate courses.
- It could occasionally recommend the same course being queried, so I added a validator that checks for self-referential results.


## Key Features
- **Automated Tag Generation**: System assigns tags from course data (department, distribution, professor, and title keywords)
- **Dynamic Filtering**: Users can add or remove tags to instantly refine visible courses
- **AI Integration**: Augmented suggestAlternatives action calls Gemini to recommend similar courses
- **Validation Guardrails**: Detects hallucinated, duplicate, or irrelevant AI outputs before display
- **Modular Design**: Core filtering, AI augmentation, and validators are implemented as independent components
- **Prompt Variants**: Three built-in modes, base, time-focused, and topic-focused, let users explore different recommendation styles

## LLM Preferences (Hardwired)
The AI is guided by these embedded assumptions in the prompt logic:
- Base Prompt: Recommends courses with general similarity in department, topic, and meeting time.
- Time-Focused Prompt: Prefers courses held at the same time as the inputed course.
- Topic-Focused Prompt: Prioritizes conceptual or thematic overlap in titles and keywords.
- Similarity Bias: Values overlap more than diversity (suggests “like with like”).
- Title-Driven Reasoning: Infers relevance mainly from course titles and tags, not full descriptions.


