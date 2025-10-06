<concept_spec>
Concept course filtering

Purpose
    Enables users to efficiently locate courses relevant to their academic goals 
    by narrowing down a large collection into a manageable set based on categories.

Principle
    Each class begins with a set of system assigned tags, and the user begins with 
    a list of all available classes. The user selects one or more tags, and the filter 
    produces a list of courses that only includes classes matching all selected tags. 
    The user can then add or remove tags and get a new list of courses that only includes 
    classes matching all selected tags. The user can then clear the filters to remove all active tags. 
    In addition to manual filtering, the user may select a course and invoke AI to suggest 
    alternative courses that share overlapping tags.

State
    A set of courses with
        A set of tags
    A set of tags with
        An id String
        A category String
    A set of Active tags
    A set of Filtered courses
    A set of Suggested courses

Actions
    AddTag (t: tag)
        effect adds tag to the active set and updates to ensure classes 
            matching all selected tags are in set of filtered courses
    RemoveTag (t: tag)
        effect removes tag from the active set of tags and updates to 
            ensure classes matching all selected tags are in set of filtered courses
    ClearTags()
        effect resets filter and clears the tags in the Active 
            set of tags and clears the courses in the set of filtered courses
    suggestAlternatives (c : course)
        requires that course to have associated tags
            effect produces a set of suggested courses that 
            share overlapping tags with the inputted course and 
            updates Suggested courses to store these suggested courses

</concept_spec>