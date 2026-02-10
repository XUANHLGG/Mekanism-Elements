package com.fxd927.mekanismelements.common.datagen;

import com.fxd927.mekanismelements.common.registries.MSBlocks;
import com.fxd927.mekanismelements.common.registries.MSItems;
import net.minecraft.core.HolderLookup;
import net.minecraft.data.PackOutput;
import net.minecraft.data.recipes.*;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.Items;
import net.minecraft.world.item.crafting.Ingredient;

import java.util.concurrent.CompletableFuture;

public class ModRecipeProvider extends RecipeProvider {

    public ModRecipeProvider(PackOutput output, CompletableFuture<HolderLookup.Provider> lookupProvider) {
        super(output, lookupProvider);
    }

    @Override
    protected void buildRecipes(RecipeOutput output) {
        // Syringe
        ShapedRecipeBuilder.shaped(RecipeCategory.MISC, MSItems.SYRINGE.get())
                .pattern(" I ")
                .pattern(" G ")
                .pattern(" G ")
                .define('I', Items.IRON_INGOT)
                .define('G', Items.GLASS_PANE)
                .unlockedBy("has_iron", has(Items.IRON_INGOT))
                .save(output);

        // High Quality Concrete Clump
        ShapelessRecipeBuilder.shapeless(RecipeCategory.BUILDING_BLOCKS, MSItems.HIGH_QUALITY_CONCRETE_CLUMP.get(), 4)
                .requires(Items.CLAY_BALL)
                .requires(Items.GRAVEL)
                .requires(Items.SAND)
                .requires(MSItems.DUST_CALCIUM_OXIDE.get())
                .unlockedBy("has_calcium_oxide", has(MSItems.DUST_CALCIUM_OXIDE.get()))
                .save(output);

        // Colored High Quality Concrete Clumps
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_AQUA.get(), Items.CYAN_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_BLACK.get(), Items.BLACK_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_BLUE.get(), Items.BLUE_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_BROWN.get(), Items.BROWN_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_CYAN.get(), Items.CYAN_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_DARK_RED.get(), Items.RED_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_GRAY.get(), Items.GRAY_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_GREEN.get(), Items.GREEN_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_LIGHT_BLUE.get(), Items.LIGHT_BLUE_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_LIGHT_GRAY.get(), Items.LIGHT_GRAY_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_LIME.get(), Items.LIME_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_MAGENTA.get(), Items.MAGENTA_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_ORANGE.get(), Items.ORANGE_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_PINK.get(), Items.PINK_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_PURPLE.get(), Items.PURPLE_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_RED.get(), Items.RED_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_WHITE.get(), Items.WHITE_DYE);
        addColorRecipe(output, MSItems.HIGH_QUALITY_CONCRETE_CLUMP_YELLOW.get(), Items.YELLOW_DYE);

        // Iodine Tablet
        ShapelessRecipeBuilder.shapeless(RecipeCategory.MISC, MSItems.TABLET_IODINE.get(), 1)
                .requires(Items.PAPER)
                .requires(MSItems.DUST_CALCIUM_OXIDE.get())
                .unlockedBy("has_calcium_oxide", has(MSItems.DUST_CALCIUM_OXIDE.get()))
                .save(output);

        // Calcium Oxide Dust
        ShapedRecipeBuilder.shaped(RecipeCategory.MISC, MSItems.DUST_CALCIUM_OXIDE.get(), 4)
                .pattern("SSS")
                .pattern("SCS")
                .pattern("SSS")
                .define('S', Items.SAND)
                .define('C', Items.COAL)
                .unlockedBy("has_sand", has(Items.SAND))
                .save(output);
    }

    private void addColorRecipe(RecipeOutput output, Item item, Item dye) {
        ShapelessRecipeBuilder.shapeless(RecipeCategory.BUILDING_BLOCKS, item, 8)
                .requires(MSItems.HIGH_QUALITY_CONCRETE_CLUMP.get(), 8)
                .requires(dye)
                .unlockedBy("has_clump", has(MSItems.HIGH_QUALITY_CONCRETE_CLUMP.get()))
                .save(output);
    }
}
