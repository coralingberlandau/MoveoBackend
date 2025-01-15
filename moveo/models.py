from django.db import models

class Codeblock(models.Model):
    """
    Model representing a code block with a title, solution, and creation date.
    """

    title = models.CharField(
        max_length=50, 
        null=True, 
        blank=True, 
        verbose_name="Title"
    )
    """
    Field: 'title'
    - Stores the title of the code block.
    - Allows up to 50 characters.
    - Can be null or left blank.
    - Displayed as 'Title' in the admin interface.
    """

    solution = models.TextField(
        null=True, 
        blank=True, 
        verbose_name="Solution"
    )

    """
    Field: 'solution'
    - Stores the solution or content of the code block.
    - Can be null or left blank.
    - Displayed as 'Solution' in the admin interface.
    """

    date_created = models.DateField(
        auto_now_add=True
    )
    
    """
    Field: 'date_created'
    - Automatically stores the date when the code block is created.
    - Not editable by users.
    """

    def __str__(self):
        """
        String representation of the Codeblock object.
        Returns the title if available, otherwise returns 'Untitled Codeblock'.
        """
        return self.title if self.title else "Untitled Codeblock"
