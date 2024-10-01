from django.contrib import admin
from .models import Project, Category, Tag, BlogPost, TestiMonial, Servie, Skill, Plan

# Register the Project model
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title', 'description')

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

# Register the Tag model
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

# Register the BlogPost model
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'is_published', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

# Register the Testimonial model
@admin.register(TestiMonial)
class TestiMonialAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')

# Register the Service model
@admin.register(Servie)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')

# Register the Skill model
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

# Register the Skill model
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
